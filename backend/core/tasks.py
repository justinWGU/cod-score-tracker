from background_task import background
from .services.update_scores import update_scores


@background()
def update_scores_task():
  """Runs update_scores as a background task outside of reques/response cycle."""
  
  print('Starting task...')
  try:
    update_scores(test=True, match_id=1)
  except Exception as e:
    print(f'Unknown error ocurred in update_scores_task: {e}')