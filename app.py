from config import Config
from interactive_bezier.interactive_bezier import App

if __name__ == "__main__":
    app = App(config=Config())
    app.setup()
    app.mainloop()
