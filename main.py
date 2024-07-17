import sqlite3
from display import HomePage, App
from intro_function import sign_up, login
from home_function import get_recommended_topics, update_stats1
from topics_function import Topics 
from study_function import get_questions, select_questions, update_delayed_questions, incorrect, correct

def main():
  #some functions were defined here, due to being used across many files
  #returns the users stats
  def get_stats(username):
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    user_stats = cursor.execute("SELECT * FROM stats WHERE username = ?", (username,)).fetchone()
    connection.close() 
    return user_stats

  #changes to the home page
  def show_home_page(username):
    update_stats1(app, get_stats)
    app.intro_page.change_pages(app.intro_page, app.tabs)
    get_recommended_topics(username, app)
  
  #implementing all of the back end logic into the front end
  app = App()
  app.intro_page.sign_up_button.configure(command=lambda: sign_up(app.intro_page.username_entry.get(), app.intro_page.username_entry.get(), update_stats1, get_stats, get_recommended_topics, app))
  app.intro_page.login_button.configure(command=lambda: login(update_stats1, get_stats, get_recommended_topics, app))
  app.home_page.update_button.configure(command=lambda: update_stats1(app, get_stats))
  topics = Topics()
  app.topics_page.add_button.configure(command=lambda: topics.add_click(app))
  app.topics_page.remove_button.configure(command=lambda: topics.remove_click(app))
  app.study_page.study_button.configure(command=lambda: select_questions(app))
  app.study_page.incorrect_button.configure(command=lambda: incorrect(app, get_stats))
  app.study_page.correct_button.configure(command=lambda: correct(app, get_stats))
  app.mainloop()

if __name__ == "__main__":
  main()



