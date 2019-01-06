import faces

class Controller(faces.controller.Controller):

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