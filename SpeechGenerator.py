from gtts import gTTS
from argparse import ArgumentParser


class SpeechGenerator(object):

    def argument_manager(self):
        parser = ArgumentParser()

        parser.add_argument("-l", "--lang",
                            action="store",
                            type=str,
                            default='en',
                            choices=['af', 'sq', 'ar', 'hy', 'bn', 'ca', 'zh',
                                     'zh-cn', 'zh-tw', 'zh-yue', 'hr', 'cs',
                                     'da', 'nl', 'en', 'en-au', 'en-uk',
                                     'en-us', 'eo', 'fi', 'fr', 'de', 'el',
                                     'hi', 'hu', 'is', 'id', 'it', 'ja', 'km',
                                     'ko', 'la', 'lv', 'mk', 'no', 'pl', 'pt',
                                     'ro', 'ru', 'sr', 'si', 'sk', 'es',
                                     'es-es', 'es-us', 'sw', 'sv', 'ta', 'th',
                                     'tr', 'uk', 'vi', 'cy'],
                            help="Set the language for the speech. Default is "
                                 "english('en').")

        parser.add_argument("-p", "--phrase",
                            action="store",
                            type=str,
                            nargs='*',
                            required=True,
                            help="Line that you want to use to create the "
                                 "speech.")

        parser.add_argument("-v", "--velocity",
                            action="store",
                            default='fast',
                            type=str,
                            choices=['fast', 'slow'],
                            help="Set the velocity of the speech. Default is "
                                 "fast.")

        parser.add_argument("-n", "--name",
                            action="store",
                            type=str,
                            default='speech',
                            help="Name of the output mp3 file. Default is "
                                 "'speech.mp3'.")

        args = parser.parse_args()

        try:
            if args.lang is not None:
                self.lang = args.lang

            if args.phrase is not None:
                phrase = " ".join(args.phrase)
                self.phrase = phrase

            if args.velocity is not None:
                if args.velocity == 'slow':
                    self.slow = True
                else:
                    self.slow = False

            if args.name is not None:
                name = args.name + ".mp3"
                self.name = name

        except Exception as e:
            print(e)

    def create_instance(self):
        self.speech_instance = gTTS(text=self.phrase, lang=self.lang,
                                    slow=self.slow)

    def save_mp3_file(self):
        print("Savind '%s' to '%s'..." % (self.phrase, self.name))
        self.speech_instance.save(self.name)

    def init(self):
        self.argument_manager()
        self.create_instance()
        self.save_mp3_file()


def main():
    speech_generator = SpeechGenerator()
    speech_generator.init()


if __name__ == "__main__":
    main()
