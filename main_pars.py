import requests
import os.path
from moviepy.editor import *
from params import names, links_id, headers


def download_content(links, names, headers):
     count = 0
# ================================ Список с названиями папок по темам ================================ #
     directory_name = []

     for id, dr_name in zip(links, names):
          count += 1

# ========================= Наполняем массив именами папок по темам занятий и создаём папки ========================= #
          if not f"{count-1} {dr_name[0]} ({dr_name[1]})" in directory_name:
               directory_name.append(f"{count} {dr_name[0]} ({dr_name[1]})")
          else:
               directory_name.append(f"{count-1}.2 {dr_name[0]} ({dr_name[1]})")

          os.mkdir(directory_name[count-1])

# ============================ Прописываем ссылки по которым качаем файлы. Подставляем id ============================ #
          video = f'https://sc.eduprof.ru/presentation/07132fff65da8c101b9468248fe3d347fbfab893-{id}/deskshare/deskshare.mp4'
          audio = f'https://sc.eduprof.ru/presentation/07132fff65da8c101b9468248fe3d347fbfab893-{id}/video/webcams.mp4'

          video_webm = f'https://sc.eduprof.ru/presentation/07132fff65da8c101b9468248fe3d347fbfab893-{id}/deskshare/deskshare.webm'
          audio_webm = f'https://sc.eduprof.ru/presentation/07132fff65da8c101b9468248fe3d347fbfab893-{id}/video/webcams.webm'


          # ================================ Скачиваем файлы ================================ #

          response_video = requests.get(video, headers=headers)
          response_audio = requests.get(audio, headers=headers)

          if response_video.status_code == 404 or response_audio.status_code == 404:
               response_video = requests.get(video_webm, headers=headers)
               response_audio = requests.get(audio_webm, headers=headers)


# ============================== Указываем пути куда сохраняем скачанные файлы. Названия папок - подставляем переменные
          # В том числе, заранее указываем путь к mp3 файлу, который ещё не сформирован ============================= #
          present_path = f"/.../{directory_name[count-1]}/video.mp4"
          sound_path = f"/home/dima/Projects/pythonProject/Front_learn/{directory_name[count-1]}/sound.mp4"
          audio_mp3_path = f"/.../{directory_name[count-1]}/audio.mp3"

# ================================ Формируем исходные (скачанные) файлы ================================ #
          with open(present_path, "wb") as file:
               file.write(response_video.content)
               file.close()

          with open(sound_path, "wb") as file:
               file.write(response_audio.content)
               file.close()

# ============================= Из файла sound.mp4 формируем звуковую дорожку audio.mp3 ============================= #
          video_path = os.path.join(sound_path)
          audio_path = os.path.join(audio_mp3_path)

          vid = VideoFileClip(video_path)
          audio = vid.audio
          audio.write_audiofile(audio_path, bitrate='128k')

# ======================= Монтируем видео, соединяя видеофайл video.mp4 и фудиофайл audio.mp3 ======================= #
          videoclip = VideoFileClip(present_path)
          audioclip = AudioFileClip(audio_mp3_path)

          new_audioclip = CompositeAudioClip([audioclip])
          videoclip.audio = new_audioclip

          # Прописываем путь и имя получившегося видеофайла
          videoclip.write_videofile(f"/.../{directory_name[count-1]}/{dr_name[0]}.mp4")

# ================================ Отчищаем папку от исходников ================================ #
          os.remove(present_path)
          os.remove(sound_path)
          os.remove(audio_mp3_path)


if __name__=='__main__':
     download_content(links_id, names, headers)

