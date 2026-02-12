#!/usr/bin/env python3
"""
Survivor Season 1 Alliance Visualization
Creates network diagrams showing voting relationships and alliances.
"""

import json
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path

def load_data(filepath='season1_analysis_results.json'):
    """Load the analysis results from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def create_network_graph(data, min_votes=2):
    """
    Create a NetworkX graph from alliance data.

    Args:
        data: Dictionary containing analysis results
        min_votes: Minimum number of votes together to include edge (default: 2)

    Returns:
        NetworkX Graph object
    """
    G = nx.Graph()

    # Add all contestants as nodes
    for contestant in data['contestants']:
        is_finalist = contestant in data['finalists']
        is_winner = contestant == data['winner']

        G.add_node(contestant,
                   finalist=is_finalist,
                   winner=is_winner)

    # Add edges for alliances (filter by minimum votes)
    for alliance in data['strong_alliances']:
        if alliance['votes_together'] >= min_votes:
            G.add_edge(alliance['player1'],
                      alliance['player2'],
                      weight=alliance['votes_together'])

    return G

def visualize_matplotlib(G, data, output_dir='visualizations'):
    """
    Create static visualization using Matplotlib.

    Args:
        G: NetworkX graph
        data: Analysis results dictionary
        output_dir: Directory to save output files
    """
    Path(output_dir).mkdir(exist_ok=True)

    # Create figure
    fig, ax = plt.subplots(figsize=(16, 12))

    # Use spring layout for force-directed positioning
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Prepare node colors and sizes
    node_colors = []
    node_sizes = []
    node_edgecolors = []
    node_linewidths = []

    for node in G.nodes():
        if G.nodes[node]['winner']:
            # Winner: Large gold with dark red border - VERY PROMINENT
            node_colors.append('#FFD700')
            node_sizes.append(4000)
            node_edgecolors.append('#8B0000')  # Dark red
            node_linewidths.append(6)
        elif G.nodes[node]['finalist']:
            # Other finalists: Large silver with dark red border - PROMINENT
            node_colors.append('#E8E8E8')
            node_sizes.append(3500)
            node_edgecolors.append('#8B0000')  # Dark red
            node_linewidths.append(5)
        else:
            # Regular contestant
            node_colors.append('#87CEEB')
            node_sizes.append(2000)
            node_edgecolors.append('#333333')
            node_linewidths.append(2)

    # Get edge weights for thickness
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    max_weight = max(weights)

    # Normalize edge widths (1-10 range)
    edge_widths = [1 + (w / max_weight) * 9 for w in weights]

    # Normalize edge colors by strength
    edge_colors = [w / max_weight for w in weights]

    # Draw edges
    nx.draw_networkx_edges(G, pos,
                          width=edge_widths,
                          alpha=0.6,
                          edge_color=edge_colors,
                          edge_cmap=plt.cm.Blues,
                          ax=ax)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos,
                          node_color=node_colors,
                          node_size=node_sizes,
                          edgecolors=node_edgecolors,
                          linewidths=node_linewidths,
                          ax=ax)

    # Draw labels
    nx.draw_networkx_labels(G, pos,
                           font_size=12,
                           font_weight='bold',
                           font_family='sans-serif',
                           ax=ax)

    # Add title with Final Tribal Council info
    analysis_type = data.get('analysis_type', 'full_season')
    type_label = "PRE-MERGE ONLY" if analysis_type == "pre_merge_only" else "Full Season"
    finalists_str = " & ".join(data['finalists'])
    title = f"Survivor Season {data['season']}: {data['season_name']} - {type_label}\n"
    title += f"Alliance Network (2+ votes together)\n"
    title += f"Final Tribal Council: {finalists_str}"
    ax.set_title(title, fontsize=20, fontweight='bold', pad=20)

    # Create legend highlighting Final Tribal Council
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD700',
               markersize=18, markeredgecolor='#8B0000', markeredgewidth=4,
               label=f'WINNER: {data["winner"]}'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#E8E8E8',
               markersize=16, markeredgecolor='#8B0000', markeredgewidth=3,
               label='Final Tribal Council'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#87CEEB',
               markersize=12, markeredgecolor='#333333', markeredgewidth=1,
               label='Pre-Merge Contestant'),
        Line2D([0], [0], color='#4A90E2', linewidth=8, alpha=0.7,
               label='Strong Alliance (5+ votes)'),
        Line2D([0], [0], color='#4A90E2', linewidth=4, alpha=0.6,
               label='Moderate Alliance (3-4 votes)'),
        Line2D([0], [0], color='#4A90E2', linewidth=2, alpha=0.5,
               label='Weak Alliance (2 votes)')
    ]

    ax.legend(handles=legend_elements, loc='upper left', fontsize=10,
             framealpha=0.95, title='Legend', title_fontsize=11)

    # Add statistics
    tc_label = "Pre-Merge Tribal Councils" if analysis_type == "pre_merge_only" else "Tribal Councils"
    stats_text = f"Contestants: {len(data['contestants'])} | "
    stats_text += f"{tc_label}: {data['total_tribal_councils']} | "
    stats_text += f"Strong Alliances: {len(data['strong_alliances'])}"

    ax.text(0.5, -0.08, stats_text,
           transform=ax.transAxes,
           ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFE4B5', alpha=0.8,
                    edgecolor='#8B4513', linewidth=2))

    ax.axis('off')
    plt.tight_layout()

    # Save outputs
    png_path = Path(output_dir) / 'season1_alliances.png'
    svg_path = Path(output_dir) / 'season1_alliances.svg'

    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(svg_path, bbox_inches='tight', facecolor='white')

    print(f"✓ Saved static visualizations:")
    print(f"  - {png_path}")
    print(f"  - {svg_path}")

    plt.close()

def visualize_plotly(G, data, output_dir='visualizations'):
    """
    Create interactive visualization using Plotly.

    Args:
        G: NetworkX graph
        data: Analysis results dictionary
        output_dir: Directory to save output files
    """
    Path(output_dir).mkdir(exist_ok=True)

    # Use spring layout (same as matplotlib for consistency)
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Create edge traces
    edge_traces = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        weight = G[edge[0]][edge[1]]['weight']

        # Edge line
        edge_trace = go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            mode='lines',
            line=dict(
                width=1 + (weight / 13) * 9,  # 13 is max votes
                color=f'rgba(100, 150, 200, {0.3 + (weight / 13) * 0.6})'
            ),
            hoverinfo='text',
            text=f'{edge[0]} ↔ {edge[1]}: {weight} votes together',
            showlegend=False
        )
        edge_traces.append(edge_trace)

    # Create node trace
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    node_sizes = []
    node_symbols = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

        # Count alliances
        alliances = list(G.neighbors(node))
        num_alliances = len(alliances)
        total_votes = sum(G[node][neighbor]['weight'] for neighbor in alliances)

        # Create hover text
        text = f"<b>{node}</b><br>"
        text += f"Alliances: {num_alliances}<br>"
        text += f"Total votes together: {total_votes}<br>"

        if G.nodes[node]['winner']:
            text += "<br><br><b>🏆 WINNER 🏆</b>"
            text += "<br>Final Tribal Council"
            node_colors.append('#FFD700')
            node_sizes.append(40)
            node_symbols.append('star')
        elif G.nodes[node]['finalist']:
            text += "<br><br><b>🥈 FINALIST 🥈</b>"
            text += "<br>Final Tribal Council"
            node_colors.append('#E8E8E8')
            node_sizes.append(35)
            node_symbols.append('diamond')
        else:
            node_colors.append('#87CEEB')
            node_sizes.append(25)
            node_symbols.append('circle')

        # Add top 3 strongest alliances
        if alliances:
            alliance_list = [(G[node][n]['weight'], n) for n in alliances]
            alliance_list.sort(reverse=True)
            text += "<br><br>Top alliances:"
            for i, (votes, partner) in enumerate(alliance_list[:3], 1):
                text += f"<br>{i}. {partner} ({votes} votes)"

        node_text.append(text)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=[node for node in G.nodes()],
        textposition='top center',
        textfont=dict(size=11, color='black', family='Arial Black'),
        hoverinfo='text',
        hovertext=node_text,
        marker=dict(
            size=node_sizes,
            color=node_colors,
            symbol=node_symbols,
            line=dict(width=3, color=['#8B0000' if c in ['#FFD700', '#E8E8E8'] else '#333333' for c in node_colors])
        ),
        showlegend=False
    )

    # Create figure
    fig = go.Figure(data=edge_traces + [node_trace])

    # Update layout
    analysis_type = data.get('analysis_type', 'full_season')
    type_label = "PRE-MERGE ONLY" if analysis_type == "pre_merge_only" else "Full Season"
    finalists_str = " & ".join(data['finalists'])
    fig.update_layout(
        title=dict(
            text=f"Survivor Season {data['season']}: {data['season_name']} - {type_label}<br>" +
                 f"<sub>Alliance Network | Final Tribal Council: {finalists_str}</sub>",
            x=0.5,
            xanchor='center',
            font=dict(size=24)
        ),
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=100),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        width=1200,
        height=900
    )

    # Add annotations for statistics
    stats_annotation = dict(
        text=f"Contestants: {len(data['contestants'])} | " +
             f"Tribal Councils: {data['total_tribal_councils']} | " +
             f"Strong Alliances: {len(data['strong_alliances'])}",
        xref='paper', yref='paper',
        x=0.5, y=-0.05,
        showarrow=False,
        font=dict(size=12),
        bgcolor='wheat',
        bordercolor='black',
        borderwidth=1
    )
    fig.add_annotation(stats_annotation)

    # Save interactive HTML
    html_path = Path(output_dir) / 'season1_alliances_interactive.html'
    fig.write_html(html_path)

    print(f"✓ Saved interactive visualization:")
    print(f"  - {html_path}")

def print_top_alliances(data, top_n=10):
    """Print the top N strongest alliances."""
    print(f"\n{'='*60}")
    print(f"TOP {top_n} STRONGEST ALLIANCES - Season {data['season']}: {data['season_name']}")
    print('='*60)

    for i, alliance in enumerate(data['strong_alliances'][:top_n], 1):
        player1 = alliance['player1']
        player2 = alliance['player2']
        votes = alliance['votes_together']

        # Add markers for finalists
        p1_marker = '🏆' if player1 == data['winner'] else ('🥈' if player1 in data['finalists'] else '')
        p2_marker = '🏆' if player2 == data['winner'] else ('🥈' if player2 in data['finalists'] else '')

        print(f"{i:2d}. {player1:12s} {p1_marker} ↔ {player2:12s} {p2_marker} : {votes:2d} votes together")

    print('='*60)

def main():
    """Main execution function."""
    print("\n🏝️  SURVIVOR SEASON 1 ALLIANCE VISUALIZATION")
    print("=" * 60)

    # Load data
    print("\n📊 Loading analysis data...")
    data = load_data('season1_analysis_results.json')
    print(f"✓ Loaded data for Season {data['season']}: {data['season_name']}")

    # Create network graph
    print("\n🕸️  Creating network graph...")
    G = create_network_graph(data, min_votes=2)
    print(f"✓ Graph created: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Print top alliances
    print_top_alliances(data)

    # Create visualizations
    print("\n🎨 Generating visualizations...")
    visualize_matplotlib(G, data)
    visualize_plotly(G, data)

    print("\n✅ VISUALIZATION COMPLETE!")
    print("\nOutput files in 'visualizations/' directory:")
    print("  - season1_alliances.png (static, high-res)")
    print("  - season1_alliances.svg (static, scalable)")
    print("  - season1_alliances_interactive.html (interactive, hoverable)")
    print("\n💡 Open the HTML file in a browser for interactive exploration!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
