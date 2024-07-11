
#0x00-MySQL_Advanced
This project focuses on advanced MySQL features and techniques. It includes tasks that cover creating and managing tables with unique constraints, enumerations, and triggers. You will work on optimizing database searches, handling user input validations, and implementing stored procedures for complex data operations. The project also involves creating views for specific data conditions and ensuring data integrity and efficiency through indexing and proper database management practices. Each task provides practical experience in handling real-world database scenarios, enhancing your skills in advanced MySQL operations.

## Tasks To Complete

| Task | Description | File |
|------|-------------|------|
| 0. **We are all unique!** | Create a table `users` with unique `email` attribute. | [0-uniq_users.sql](0-uniq_users.sql) |
| 1. **In and not out** | Create a table `users` with `country` attribute as enumeration. | [1-country_users.sql](1-country_users.sql) |
| 2. **Best band ever!** | Rank country origins of bands by number of fans. | [2-fans.sql](2-fans.sql) |
| 3. **Old school band** | List bands with `Glam rock` as main style by longevity. | [3-metal_bands.sql](3-metal_bands.sql) |
| 4. **Buy buy buy** | Create a trigger to decrease item quantity after adding a new order. | [4-store.sql](4-store.sql) |
| 5. **Email validation to sent** | Create a trigger to reset `valid_email` attribute only when `email` is changed. | [5-valid_email.sql](5-valid_email.sql) |
| 6. **Add bonus** | Create a stored procedure `AddBonus` to add a new correction for a student. | [6-bonus.sql](6-bonus.sql) |
| 7. **Average score** | Create a stored procedure `ComputeAverageScoreForUser` to compute and store average score for a student. | [7-average_score.sql](7-average_score.sql) |
| 8. **Optimize simple search** | Create an index `idx_name_first` on the table `names` for the first letter of `name`. | [8-index_my_names.sql](8-index_my_names.sql) |
| 9. **Optimize search and score** | Create an index `idx_name_first_score` on the table `names` for the first letter of `name` and `score`. | [9-index_name_score.sql](9-index_name_score.sql) |
| 10. **Safe divide** | Create a function `SafeDiv` to divide two numbers or return 0 if the second number is 0. | [10-div.sql](10-div.sql) |
| 11. **No table for a meeting** | Create a view `need_meeting` to list students with score under 80 and no `last_meeting` or more than 1 month. | [11-need_meeting.sql](11-need_meeting.sql) |
| 12. **Average weighted score** | Create a stored procedure `ComputeAverageWeightedScoreForUser` to compute and store the average weighted score for a student. | [100-average_weighted_score.sql](100-average_weighted_score.sql) |
| 13. **Average weighted score for all!** | Create a stored procedure `ComputeAverageWeightedScoreForUsers` to compute and store the average weighted score for all students. | [101-average_weighted_score.sql](101-average_weighted_score.sql) |


