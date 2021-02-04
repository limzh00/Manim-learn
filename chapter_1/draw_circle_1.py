from manimlib.imports import *
import math

class FollowingGraphCamera(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        self.play(ShowCreationThenFadeOut(TextMobject("BackSpace")))
        self.camera_frame.save_state()
        self.setup_axes(animate=False)
        graph = self.get_graph(lambda x: np.sin(x),
                               color=BLUE,
                               x_min=0,
                               x_max=3 * PI
                               )
        moving_dot = Dot().move_to(graph.points[0]).set_color(ORANGE)

        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_grap = Dot().move_to(graph.points[-1])
        self.add(graph, dot_at_end_grap, dot_at_start_graph, moving_dot)
        self.play( self.camera_frame.scale,0.5,self.camera_frame.move_to,moving_dot)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera_frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera_frame.remove_updater(update_curve)

        self.play(Restore(self.camera_frame))




    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph_2(self, x):
        return(x**3)