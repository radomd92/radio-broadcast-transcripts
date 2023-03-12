import os
import sys
import textwrap
import whisper
import time


class Transcriptor:

    CHARACTERS_PER_LINE = 80

    def __init__(self, model):
        self.model = model

    def run(self, path):
        out_file_path = path.replace('.mp3', '.txt')    
        if os.path.exists(out_file_path):
            print(f"Skipping {out_file_path}: file exists")
            return

        result = self.model.transcribe(path)
        text = result["text"]
        with open(out_file_path, 'w') as out_file:
            out_file.write(f'TRANSCRIPTION: {path.upper()}\n')
            out_file.write('-' * self.CHARACTERS_PER_LINE + '\n')
            out_file.write('\n'.join(textwrap.wrap(text, width=self.CHARACTERS_PER_LINE)))


if __name__ == '__main__':
    file_paths = sys.argv[1:]
    print(file_paths)
    
    model_name='large-v2'
    #model_name='small.en'
    t0 = time.time()
    print(f"[{time.time() - t0}] Loading model...")
    model = whisper.load_model(model_name)
    print(f"[{time.time() - t0}] Loaded model...")
    

    worker = Transcriptor(model)
    t0 = time.time()
    for file_path in file_paths:
        print(f"[{time.time() - t0}] Running on {file_path}...")        
        try:
            worker.run(file_path)
        except Exception as error:
            print(error)
            continue
        print(f"[{time.time() - t0}] Finished {file_path}...")
        t0 = time.time()
