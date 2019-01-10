import faces

class Controller(faces.controller.Controller):

    def on_start(self):
        self.btn = self.find_widget('#btn')
        self.btn.add_event('click', self.on_btn_clicked)

    def plurarize(self, text, value):
        if value == 1:
            return text
        else:
            return f'{text}s'

    def on_btn_clicked(self):
        self.count +=1
        self.btn.set_property('text', f"You\'ve clicked me {self.count} {self.plurarize('time', self.count)}")

    @property
    def design(self):
        return '''
            <design>
                <screen>
                    <text class="title">Hi,</text>
                    <text class="sub">I'm faces</text>
                    <text class="sub">
                        A library for building
                        desktop apps easily, in a reactive way :)
                    </text>
                    <button id="btn">Click me</button>
                </screen>

                <style>
                    screen {
                        size: 600px 300px;
                    }

                    .title {
                        font: bold 32px Arial;
                    }

                    .sub {
                        font: 14px Arial;
                        color: #444;
                    }

                    #btn {
                        background-color: #1144AA;
                        font: 16px Arial;
                        color: #fff;
                    }

                </style>
            </design>
        '''
    
    @property
    def name(self):
        return 'main'
    
    @property
    def title(self):
        return 'Hello!'


if __name__ == '__main__':
    app = faces.app.create_app([Controller])
    app.start()