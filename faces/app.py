import faces


class App:
    '''
    The `App` class is responsible for bootstrapping all UI of your application.
    It will create a instance for every controller in `controllers` and prepare 
    a window for `entry_point`, requesting a drawer.

    '''

    def __init__(self, controllers, entry_point = None):
        self.controllers = controllers
        self.controller_instances = {}

        self.entry_point = entry_point
        self.drawer = faces.drawers.TkinterDrawer()


    def start(self):
        '''
        This method searches for an `entry_point` and if found, 
        creates a window for the Controller.

        If `entry_point` isn't found, it raises an `EntryPointNotFound`
        If `entry_point` isn't set, the first controller will start application.

        '''
        for controller in self.controllers:
            instance = controller()

            instance.redraw_method = self.drawer.redraw

            self.controller_instances[controller] = instance
            
            if instance.name == self.entry_point:
                self._create_window_for(instance)
                
                instance.on_start()
                self.drawer.finish_setup()

        self._create_window_for(self.controller_instances[self.controllers[0]])
        
        instance.on_start()
        self.drawer.apply_events(instance.abstract_screen)
        self.drawer.finish_setup()
        

    def _create_window_for(self, controller):
        '''
        Creates a window for a `controller` calling a drawer.
        '''
        self.drawer.prepare()

        self.drawer.draw_screen(controller.title, controller.abstract_screen)
        self.drawer.apply_style(controller.abstract_style)


def create_app(controllers, entry_point = None):
    '''
    `create_app` creates an App instance.
    '''
    return App(controllers, entry_point)