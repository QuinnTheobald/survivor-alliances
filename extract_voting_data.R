# Extract Survivor voting data for seasons 21-25
# Install and run this script in R to get pre-merge voting data

# Install package if needed
if (!require("survivoR")) {
  install.packages("survivoR")
}
if (!require("dplyr")) {
  install.packages("dplyr")
}

library(survivoR)
library(dplyr)

# Season merge episodes (from season_metadata.py)
merge_episodes <- data.frame(
  season = c(21, 22, 23, 24, 25),
  merge_ep = c(8, 8, 8, 7, 7)
)

# Get all voting history
all_votes <- vote_history %>%
  filter(version == "US", season %in% 21:25)

# Join with merge episode data and filter for pre-merge only
pre_merge_votes <- all_votes %>%
  left_join(merge_episodes, by = "season") %>%
  filter(episode < merge_ep) %>%
  select(season, season_name, episode, day, tribe, castaway, vote, voted_out)  %>%
  arrange(season, episode, castaway)

# Export to CSV
write.csv(pre_merge_votes, "seasons_21-25_premerge_votes.csv", row.names = FALSE)

cat("\nData exported to: seasons_21-25_premerge_votes.csv\n")
cat(sprintf("Total votes extracted: %d\n", nrow(pre_merge_votes)))
cat("\nSample data:\n")
print(head(pre_merge_votes, 20))
