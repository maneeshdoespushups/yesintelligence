# Sample spinner app in kivy
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout

from kivy.app import App

# Make an App by deriving from the App class
class SpinnerExampleApp(App):
    def build(self):
        layout = FloatLayout()

        # configure spinner object and add to layout
        spinner = Spinner(
        text='What do you believe your intelligence level is at?',
        # available values
        values=(str(10*i)+ ' %' if i <= 10 else 'Yes' if i == 11 else 'No' for i in range(13)),
        # just for positioning in our example
        size_hint=(None, None),
        size=(250, 44),
        pos_hint={'center_x': .5, 'center_y': .5})

        layout.add_widget(spinner)
        spinner.bind(text=self.on_spinner_select)

        # add a label displaying the selection from the spinner
        self.spinnerSelection = Label()
        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint={'x': 0, 'y':.1}

        return layout;

    # call back for the selection in spinner object
    def on_spinner_select(self, spinner, text):
        self.spinnerSelection.text = "Your intelligence level is: %s"%spinner.text
        #print('The spinner', spinner, 'have text', text)


# Run the app
if __name__ == '__main__':
    SpinnerExampleApp().run()
