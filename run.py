from config import Config
from interactive_bezier.app import App

if __name__ == "__main__":
    app = App(config=Config())
    app.setup()
    app.mainloop()
