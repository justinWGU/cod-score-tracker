from background_task import background
from .services.update_scores import update_scores


@background()
def test_task():
  print('Starting task...')
  update_scores(test=True, match_id=1, live=False)