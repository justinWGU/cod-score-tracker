from background_task import background
from .services.update_scores import update_scores, update_rand_scores


@background()
def update_scores_task():
  """ Runs update_scores as a background task outside of request/response cycle. """
  
  print('Starting task...')
  try:
    update_scores(1)
  except Exception as e:
    print(f'Unknown error ocurred in update_scores_task: {e}')

@background()
def update_rand_scores_task():
  update_rand_scores()