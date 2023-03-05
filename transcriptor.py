import sys
import textwrap
import whisper


class Transcriptor:

    CHARACTERS_PER_LINE = 120

    def __init__(self, model_name='medium.en'):
        self.model = whisper.load_model(model_name)

    def run(self, path):
        result = self.model.transcribe(path)
        text = result["text"]
        with open(path.replace('.mp3', '.txt'), 'w') as out_file:
            out_file.write(f'TRANSCRIPTION: {path.upper()}\n')
            out_file.write('-' * self.CHARACTERS_PER_LINE + '\n')
            out_file.write('\n'.join(textwrap.wrap(text, width=self.CHARACTERS_PER_LINE)))


if __name__ == '__main__':
    file_path = sys.argv[1]
    worker = Transcriptor()
    worker.run(file_path)
