import os
import sys
import textwrap
import whisper
import time
import traceback


class Transcriptor:

    CHARACTERS_PER_LINE = 80

    def __init__(self, model):
        self.model = model

    def run(self, path, language='en'):
        out_file_path = ''.join(path.split('.')[:-1]) + '.txt'
        
        if os.path.exists(out_file_path):
            print(f"Skipping {out_file_path}: file exists")
            return

        result = self.model.transcribe(path, language=language)
        text = result["text"]
        with open(out_file_path.replace('_audio', ''), 'w') as out_file:
            out_file.write(f'TRANSCRIPTION: {path.upper()}\n')
            out_file.write('-' * self.CHARACTERS_PER_LINE + '\n')
            out_file.write('\n'.join(textwrap.wrap(text, width=self.CHARACTERS_PER_LINE)))


def main():
    language = sys.argv[1]
    file_paths = sys.argv[2:]
    print(language, file_paths)
    
    model_name='large'
    #model_name='small.en'
    t0 = time.time()
    print(f"[{time.time() - t0}] Loading model...")
    model = whisper.load_model(model_name)
    print(f"[{time.time() - t0}] Loaded model...")
    
    try:
        worker = Transcriptor(model)
        t0 = time.time()
        for file_path in file_paths:
            print(f"[{time.time() - t0}] Running on {file_path}...")        
            try:
                worker.run(file_path, language=language)
            except Exception as error:
                traceback.print_exc()

            print(f"[{time.time() - t0}] Finished {file_path}...")
            t0 = time.time()
    finally:
        model.cpu()
        del model.encoder
        del model.decoder
        del model
        whisper.torch.cuda.empty_cache()

    
if __name__ == '__main__':
    try:
        main()
    finally:
        print("Bye!")