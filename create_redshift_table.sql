CREATE table pred_results (
  datetime timestamp,
  color_A varchar(10), 
  color_B varchar(10),
  decision char(1),
  odds_A smallint,
  odds_B smallint,
  pct_users_A smallint,
  pct_users_B smallint,
  title_A varchar(100),
  title_B varchar(100),
  channel_id int,
  event_id varchar(100),
  type varchar(100));
