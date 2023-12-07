from config import Config
from interactive_bezier.app import App

if __name__ == "__main__":
    try:
        app = App(config=Config())
        app.setup()
        app.mainloop()
    except Exception as e:
        print(f"Runtime error: {e}")
