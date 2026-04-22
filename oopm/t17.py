
class demo :
    def _self(self):
        print(" i am a protected function")

    def __self(self):
        print('i am a private functions')
    def self(self):
        print('i am a public functions')



if __name__ == "__main__" :
    s = demo()
    s.self() # run public function
    s._self() # run protected function
    # s.__self() # AttributeError: 'demo' object has no attribute '__self'. Did you mean: '_self'?
