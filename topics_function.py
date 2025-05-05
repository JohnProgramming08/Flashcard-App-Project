from contextlib import suppress


class Topics():
  def __init__(self):
    self.chosen_topics = []

  # Add/remove topics from the array
  def click(self, selected_topics, clicked):
    if clicked == 1:
      for topic in selected_topics:
        if topic not in self.chosen_topics:
          self.chosen_topics.append(topic)
          
      return self.chosen_topics

    for topic in selected_topics:
      with suppress(ValueError):
        self.chosen_topics.remove(topic)
        
    return self.chosen_topics

  # Display all chosen topics
  def show_topics(self, app):
    topics = ""
    for topic in self.chosen_topics:
      topics += f"{topic}\n"
  
    app.topics_page.chosen_topics.configure(text=topics)

  # Add selected topics to the list
  def add_click(self, app):
    selected_topics = app.topics_page.selected_topics
    selected_topics = self.click(selected_topics, 1)
    self.show_topics(app)

  # Remove selected topics from the list
  def remove_click(self, app):
    selected_topics = app.topics_page.selected_topics
    selected_topics = self.click(selected_topics, 0)
    self.show_topics(app)

