"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.now_playing = None
        self._pause = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos:")

        for allvideo in all_videos:
            tagString = str(allvideo.tags)
            print(allvideo.title,"("+allvideo.video_id+")","["+tagString.strip("()").replace(',', '').replace("'","")+"]")
        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        """print("play_video needs implementation")"""

        video = self._video_library.get_video(video_id)
        if video is None:
          print("Cannot play video: Video does not exist")
          return
        
        if self.now_playing:
          self.stop_video()
        print(f"Playing video: {video.title}")
        self.now_playing = video

    def stop_video(self):
        """Stops the current video."""
        if self.now_playing is None:
          print("Cannot stop video: No video is currently playing")
          return
        print(f"Stopping video: {self.now_playing.title}")
        self.now_playing = None
        self._paused = False


    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        random_idx = random.randrange(0,len(all_videos)-1)
        video_id = all_videos[random_idx].video_id
        
        self.play_video(video_id)
        
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        video = self.now_playing

        if video is None:
            print("Cannot pause video: No video is currently playing")
            return
        if self._pause is True:
            print(f"Video already paused: {video.title}")
        else:
            print(f"Pausing video: {video.title}")
            self._pause = True

    def continue_video(self):
        """Resumes playing the current video."""
        video = self.now_playing

        if video is None:
            print("Cannot continue video: No video is currently playing")
            return
        if self._pause is False:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {video.title}")
            self._pause = False


        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        
        video = self.now_playing
        

        if video is None :
            print("No video is currently playing")
            return
        else:
            tagString = str(video.tags)
            if self._pause is True:
                print("Currently playing:",video.title,"("+video.video_id+")","["+tagString.strip("()").replace(',', '').replace("'","")+"]","- PAUSED")
            else:
                print("Currently playing:",video.title,"("+video.video_id+")","["+tagString.strip("()").replace(',', '').replace("'","")+"]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
