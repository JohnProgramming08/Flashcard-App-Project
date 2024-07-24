import sqlite3

from display import App
from home_function import get_recommended_topics, update_stats2
from intro_function import login, sign_up
from study_function import correct, incorrect, select_questions
from topics_function import Topics


def main():
  # Some functions are defined here due to being used across many files
  # Return the users stats
  def get_stats(username):
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stats WHERE username = ?", (username,))
    user_stats = cursor.fetchone()
    connection.close() 
    return user_stats

  # Change to the home page
  def show_home_page(username):
    update_stats2(app, get_stats)
    app.intro_page.change_pages(app.intro_page, app.tabs)
    get_recommended_topics(username, app)
  
  # Implement all of the back end logic into the front end
  app = App()
  app.intro_page.sign_up_button.configure(command=lambda: sign_up(app.intro_page.username_entry.get(), app.intro_page.username_entry.get(), update_stats2, get_stats, get_recommended_topics, app))
  app.intro_page.login_button.configure(command=lambda: login(update_stats2, get_stats, get_recommended_topics, app))
  app.home_page.update_button.configure(command=lambda: update_stats2(app, get_stats))
  topics = Topics()
  app.topics_page.add_button.configure(command=lambda: topics.add_click(app))
  app.topics_page.remove_button.configure(command=lambda: topics.remove_click(app))
  app.study_page.study_button.configure(command=lambda: select_questions(app))
  app.study_page.incorrect_button.configure(command=lambda: incorrect(app, get_stats))
  app.study_page.correct_button.configure(command=lambda: correct(app, get_stats))
  app.mainloop()

if __name__ == "__main__":
  main()


