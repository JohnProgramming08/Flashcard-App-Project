from contextlib import suppress

class Topics:
  def __init__(self):
    self.chosen_topics = []

  #add/remove topics from the array
  def click(self, selected_topics, clicked):
    if clicked == 1:
      for i in selected_topics:
        if i in self.chosen_topics:
          break
        self.chosen_topics.append(i)

    if clicked == 0:
      for i in selected_topics:
        with suppress(ValueError):
          self.chosen_topics.remove(i)

