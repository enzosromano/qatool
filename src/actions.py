import customtkinter
import scripts.test_ex

class ExampleActions():
    def fillbox(self):
        self.textbox_ex.delete("0.0", 'end')
        self.textbox_ex.insert("0.0", "Did you notice that when you clicked the button the text changed?")