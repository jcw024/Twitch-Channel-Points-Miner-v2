EVENT_CREATED = {   'data': {   'decision': 'B',
                'event': {   'channel_id': '36340781',
                             'created_at': '2021-12-22T03:36:59.439133914Z',
                             'created_by': {   'extension_client_id': None,
                                               'type': 'USER',
                                               'user_display_name': 'CrabbyPratty',
                                               'user_id': '105769424'},
                             'ended_at': None,
                             'ended_by': None,
                             'id': '60d53297-bb6d-4e38-866e-6b131f310220',
                             'locked_at': None,
                             'locked_by': None,
                             'outcomes': [   {   'color': 'BLUE',
                                                 'id': 'f272b4aa-533f-4bd1-8fb6-c944ba2ff8e3',
                                                 'odds': 1.96,
                                                 'odds_percentage': 51.02,
                                                 'percentage_users': 51.68,
                                                 'title': 'winsum',
                                                 'top_points': 250000,
                                                 'total_points': 799204,
                                                 'total_users': 77},
                                             {   'color': 'PINK',
                                                 'id': '0010dcb8-5160-4a7a-8a10-5c93ba26fceb',
                                                 'odds': 2.04,
                                                 'odds_percentage': 49.02,
                                                 'percentage_users': 48.32,
                                                 'title': 'losesum',
                                                 'top_points': 100000,
                                                 'total_points': 769078,
                                                 'total_users': 72}],
                             'prediction_window_seconds': 120,
                             'status': 'ACTIVE',
                             'title': 'EZ DUB OR FAT L???',
                             'winning_outcome_id': None},
                'event_A': 'winsum (BLUE), Points: 799k, Users: 77 (51.68%), '
                           'Odds: 1.96 (51.02%)',
                'event_B': 'losesum (PINK), Points: 769k, Users: 72 (48.32%), '
                           'Odds: 2.04 (49.02%)',
                'timestamp': '2021-12-22T03:36:59.453234507Z'},
    'type': 'event-created'}

PREDICTION_RESULT = {'data': {'color_A': 'BLUE',
          'color_B': 'PINK',
          'decision': 'A',
          'event_A': 'Yes, he will win. (BLUE), Points: 6M, Users: 344 '
                     '(47.65%), Odds: 2.83 (35.34%)',
          'event_B': 'No, he will lose. (PINK), Points: 11M, Users: 378 '
                     '(52.35%), Odds: 1.55 (64.52%)',
          'odds_A': 2.83,
          'odds_B': 1.55,
          'pct_users_A': 47.65,
          'pct_users_B': 52.35,
          'prediction': {'channel_id': '51496027',
                         'event_id': '78b853c2-034c-4f4d-bbde-e9e136207f4e',
                         'id': 'ab98d457a1515c2c005945f9c09761bf610a0250720ea75d759c6d93990c9b02',
                         'outcome_id': '5e68f359-dc99-4acc-80a8-d5c1399c1c00',
                         'points': 2906,
                         'predicted_at': '2021-12-28T04:30:55.252462204Z',
                         'result': {'is_acknowledged': False,
                                    'points_won': None,
                                    'type': 'LOSE'},
                         'updated_at': '2021-12-28T04:57:27.339098025Z',
                         'user_display_name': None,
                         'user_id': '161606623'},
          'timestamp': '2021-12-28T04:57:27.344101075Z',
          'title_A': 'Yes, he will win.',
          'title_B': 'No, he will lose.'},
 'type': 'prediction-result'}

POINTS_SPENT = {   'data': {   'balance': {   'balance': 4329,
                               'channel_id': '36340781',
                               'user_id': '161606623'},
                'timestamp': '2021-12-22T03:38:53.670580738Z'},
    'type': 'points-spent'}

POINTS_EARNED = {   'data': {   'balance': {   'balance': 5950,
                               'channel_id': '118241089',
                               'user_id': '161606623'},
                'channel_id': '118241089',
                'point_gain': {   'baseline_points': 10,
                                  'channel_id': '118241089',
                                  'multipliers': [],
                                  'reason_code': 'WATCH',
                                  'total_points': 10,
                                  'user_id': '161606623'},
                'timestamp': '2021-12-22T03:39:56.028270388Z'},
    'type': 'points-earned'}

CLAIM_AVAILABLE = {   'data': {   'claim': {   'channel_id': '51496027',
                             'created_at': '2021-12-22T03:42:21Z',
                             'id': '9b0d7692-4eca-4f4f-afa4-4357d154f90d',
                             'point_gain': {   'baseline_points': 50,
                                               'channel_id': '51496027',
                                               'multipliers': [],
                                               'reason_code': 'CLAIM',
                                               'total_points': 50,
                                               'user_id': '161606623'},
                             'user_id': '161606623'},
                'timestamp': '2021-12-22T03:42:25.599400593Z'},
    'type': 'claim-available'}

CLAIM_CLAIMED = {   'data': {   'claim': {   'channel_id': '51496027',
                             'created_at': '2021-12-22T03:42:21Z',
                             'id': '9b0d7692-4eca-4f4f-afa4-4357d154f90d',
                             'point_gain': {   'baseline_points': 50,
                                               'channel_id': '51496027',
                                               'multipliers': [],
                                               'reason_code': 'CLAIM',
                                               'total_points': 50,
                                               'user_id': '161606623'},
                             'user_id': '161606623'},
                'timestamp': '2021-12-22T03:42:25.784998119Z'},
    'type': 'claim-claimed'}

