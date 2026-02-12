#!/usr/bin/env python3
"""
Batch Visualization Script for Multiple Seasons
Creates network diagrams for all analyzed seasons
"""

import json
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path

def load_season_results(season_num, data_dir='data/seasons'):
    """Load analysis results for a season."""
    results_file = Path(data_dir) / f"season{season_num:02d}" / "analysis_results.json"

    if not results_file.exists():
        return None

    with open(results_file, 'r') as f:
        return json.load(f)

def create_network_graph(data, min_votes=2):
    """Create NetworkX graph from alliance data."""
    G = nx.Graph()

    # Add nodes
    for contestant in data['contestants']:
        is_finalist = contestant in data['finalists']
        is_winner = contestant == data['winner']
        G.add_node(contestant, finalist=is_finalist, winner=is_winner)

    # Add edges
    for alliance in data['strong_alliances']:
        if alliance['votes_together'] >= min_votes:
            G.add_edge(alliance['player1'], alliance['player2'],
                      weight=alliance['votes_together'])

    return G

def visualize_season(season_num, data, output_dir='visualizations'):
    """Create visualization for a single season."""
    print(f"\n  Creating visualizations for Season {season_num}: {data['season_name']}")

    # Create season subdirectory
    season_dir = Path(output_dir) / f"season{season_num:02d}"
    season_dir.mkdir(parents=True, exist_ok=True)

    # Create network graph
    G = create_network_graph(data)

    if G.number_of_edges() == 0:
        print(f"    ⚠ No alliances to visualize (no edges)")
        return

    # Create matplotlib visualization
    fig, ax = plt.subplots(figsize=(16, 12))
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Node styling - Emphasize Final Tribal Council participants
    node_colors = []
    node_sizes = []
    node_edgecolors = []
    node_linewidths = []

    for node in G.nodes():
        # Get node attributes with defaults
        is_winner = G.nodes[node].get('winner', False)
        is_finalist = G.nodes[node].get('finalist', False)

        if is_winner:
            # Winner: Large gold star-like appearance
            node_colors.append('#FFD700')
            node_sizes.append(4000)
            node_edgecolors.append('#8B0000')  # Dark red border
            node_linewidths.append(6)
        elif is_finalist:
            # Other finalists: Large silver with prominent border
            node_colors.append('#E8E8E8')
            node_sizes.append(3500)
            node_edgecolors.append('#8B0000')  # Dark red border
            node_linewidths.append(5)
        else:
            # Regular contestants: Smaller, blue
            node_colors.append('#87CEEB')
            node_sizes.append(2000)
            node_edgecolors.append('#333333')
            node_linewidths.append(2)

    # Edge styling
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    max_weight = max(weights) if weights else 1
    edge_widths = [1 + (w / max_weight) * 9 for w in weights]
    edge_colors = [w / max_weight for w in weights]

    # Draw
    nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6,
                          edge_color=edge_colors, edge_cmap=plt.cm.Blues, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,
                          edgecolors=node_edgecolors, linewidths=node_linewidths, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=ax)

    # Title with Final Tribal Council info
    finalists_str = " & ".join(data['finalists'])
    title = f"Survivor Season {data['season']}: {data['season_name']} - PRE-MERGE ONLY\n"
    title += f"Alliance Network (2+ votes together)\n"
    title += f"Final Tribal Council: {finalists_str}"
    ax.set_title(title, fontsize=18, fontweight='bold', pad=20)

    # Add legend highlighting FTC participants
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

    # Stats at bottom
    stats_text = f"Contestants: {len(data['contestants'])} | "
    stats_text += f"Pre-Merge Tribal Councils: {data['total_tribal_councils']} | "
    stats_text += f"Strong Alliances: {len(data['strong_alliances'])}"
    ax.text(0.5, -0.08, stats_text, transform=ax.transAxes,
           ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFE4B5', alpha=0.8, edgecolor='#8B4513', linewidth=2))

    ax.axis('off')
    plt.tight_layout()

    # Save
    png_path = season_dir / f"season{season_num:02d}_alliances.png"
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"    ✓ Saved PNG: {png_path}")

    # Create interactive plotly version
    create_interactive_viz(season_num, data, G, pos, season_dir)

def create_interactive_viz(season_num, data, G, pos, output_dir):
    """Create interactive plotly visualization."""
    edge_traces = []

    max_weight = max([G[u][v]['weight'] for u, v in G.edges()]) if G.number_of_edges() > 0 else 1

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        weight = G[edge[0]][edge[1]]['weight']

        edge_trace = go.Scatter(
            x=[x0, x1, None], y=[y0, y1, None],
            mode='lines',
            line=dict(width=1 + (weight / max_weight) * 9,
                     color=f'rgba(100, 150, 200, {0.3 + (weight / max_weight) * 0.6})'),
            hoverinfo='text',
            text=f'{edge[0]} ↔ {edge[1]}: {weight} votes',
            showlegend=False
        )
        edge_traces.append(edge_trace)

    # Node trace
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    node_sizes = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

        alliances = list(G.neighbors(node))
        num_alliances = len(alliances)
        total_votes = sum(G[node][n]['weight'] for n in alliances) if alliances else 0

        # Get node attributes with defaults
        is_winner = G.nodes[node].get('winner', False)
        is_finalist = G.nodes[node].get('finalist', False)

        text = f"<b>{node}</b><br>Alliances: {num_alliances}<br>Total votes: {total_votes}"

        if is_winner:
            text += "<br><br><b>🏆 WINNER 🏆</b>"
            text += "<br>Final Tribal Council"
            node_colors.append('#FFD700')
            node_sizes.append(40)
        elif is_finalist:
            text += "<br><br><b>🥈 FINALIST 🥈</b>"
            text += "<br>Final Tribal Council"
            node_colors.append('#E8E8E8')
            node_sizes.append(35)
        else:
            node_colors.append('#87CEEB')
            node_sizes.append(25)

        node_text.append(text)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=[node for node in G.nodes()],
        textposition='top center',
        textfont=dict(size=10, color='black', family='Arial Black'),
        hoverinfo='text',
        hovertext=node_text,
        marker=dict(size=node_sizes, color=node_colors,
                   line=dict(width=3, color=['#8B0000' if c in ['#FFD700', '#E8E8E8'] else '#333333' for c in node_colors])),
        showlegend=False
    )

    fig = go.Figure(data=edge_traces + [node_trace])

    finalists_str = " & ".join(data['finalists'])
    fig.update_layout(
        title=dict(
            text=f"Season {data['season']}: {data['season_name']} - PRE-MERGE<br>" +
                 f"<sub>Interactive Alliance Network | Final Tribal Council: {finalists_str}</sub>",
            x=0.5, xanchor='center', font=dict(size=20)
        ),
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20, l=5, r=5, t=80),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        width=1000, height=800
    )

    html_path = output_dir / f"season{season_num:02d}_interactive.html"
    fig.write_html(html_path)
    print(f"    ✓ Saved HTML: {html_path}")

def create_comparison_summary(seasons_data, output_dir='visualizations'):
    """Create a summary comparison of all seasons."""
    print("\n  Creating comparison summary...")

    # Create summary data
    summary = []
    for data in seasons_data:
        summary.append({
            'season': data['season'],
            'name': data['season_name'],
            'year': data['year'],
            'alliances': len(data['strong_alliances']),
            'winner': data['winner']
        })

    # Create bar chart
    fig, ax = plt.subplots(figsize=(14, 8))

    seasons = [s['season'] for s in summary]
    alliance_counts = [s['alliances'] for s in summary]
    names = [f"S{s['season']}: {s['name']}" for s in summary]

    bars = ax.bar(range(len(seasons)), alliance_counts, color='#4A90E2', alpha=0.8)

    ax.set_xlabel('Season', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Strong Alliances (2+ votes)', fontsize=12, fontweight='bold')
    ax.set_title('Survivor Seasons 1-10: Pre-Merge Alliance Comparison',
                fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(range(len(seasons)))
    ax.set_xticklabels(names, rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()

    summary_path = Path(output_dir) / 'seasons_comparison.png'
    plt.savefig(summary_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"    ✓ Saved comparison: {summary_path}")

def main():
    """Main execution function."""
    print("🎨 SURVIVOR BATCH VISUALIZATION")
    print("Creating network diagrams for all analyzed seasons")
    print("=" * 70)

    # Find all analyzed seasons
    data_dir = Path('data/seasons')
    seasons_data = []

    for season_dir in sorted(data_dir.glob('season*')):
        results_file = season_dir / 'analysis_results.json'
        if results_file.exists():
            with open(results_file, 'r') as f:
                data = json.load(f)
                seasons_data.append(data)

    if not seasons_data:
        print("\n✗ No analyzed season data found.")
        print("  Run 'python batch_analyze.py' first to analyze seasons.")
        return

    print(f"\nFound {len(seasons_data)} analyzed season(s)")

    # Visualize each season
    for data in seasons_data:
        visualize_season(data['season'], data)

    # Create comparison if multiple seasons
    if len(seasons_data) > 1:
        create_comparison_summary(seasons_data)

    print("\n" + "=" * 70)
    print(f"✅ BATCH VISUALIZATION COMPLETE!")
    print(f"   Created visualizations for {len(seasons_data)} season(s)")
    print(f"   Output directory: visualizations/")
    print("=" * 70)

if __name__ == "__main__":
    main()
