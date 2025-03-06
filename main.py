from manim import *

class demo(Scene):
    def construct(self):
        t = Text("I am a flower")
        self.play(Write(t))
        self.wait(3)
        
