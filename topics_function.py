from contextlib import suppress

class Topics():
  def __init__(self):
    self.chosen_topics = []

  #add/remove topics from the array
  def click(self, selected_topics, clicked):
    if clicked == 1:
      for i in selected_topics:
        if i in self.chosen_topics:
          pass
          
        else:
          self.chosen_topics.append(i)
          
      return self.chosen_topics

    for i in selected_topics:
      with suppress(ValueError):
        self.chosen_topics.remove(i)
        
    return self.chosen_topics

  #displays all chosen topics
  def show_topics(self, app):
    topics = ""
    for i in self.chosen_topics:
      topics += f"{i}\n"
  
    app.topics_page.chosen_topics.configure(text=topics)

  #adds selected topics to the list
  def add_click(self, app):
    selected_topics = app.topics_page.selected_topics
    selected_topics = self.click(selected_topics, 1)
    self.show_topics(app)

  #removes selected topics from the list
  def remove_click(self, app):
    selected_topics = app.topics_page.selected_topics
    selected_topics = self.click(selected_topics, 0)
    self.show_topics(app)

