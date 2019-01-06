import faces


class App:
    '''
    The `App` class is responsible for bootstrapping all UI of your application.
    It will create a instance for every controller in `controllers` and prepare 
    a window for `entry_point`, requesting a drawer.

    '''

    def __init__(self, controllers, entry_point):
        self.controllers = controllers
        self.entry_point = entry_point
        self.drawer = faces.drawers.TkinterDrawer()

    def start(self):
        '''
        This method searches for an `entry_point` and if found, 
        creates a window for the Controller.

        If `entry_point` isn't found, it raises a `EntryPointNotFound`
        '''
        for controller in self.controllers:
            instance = controller()
            
            if instance.name == self.entry_point:
                self._create_window_for(instance)
                
                return
        
        raise faces.exceptions.EntryPointNotFound(self.entry_point)

    def _create_window_for(self, controller):
        '''
        Creates a window for a `controller` calling a drawer.
        '''
        self.drawer.prepare()

        self.drawer.draw_screen(controller.title, controller.abstract_screen)
        self.drawer.apply_style(controller.abstract_style)

        self.drawer.finish_setup()



def create_app(controllers, entry_point):
    '''
    `create_app` creates an App instance.
    '''
    return App(controllers, entry_point)