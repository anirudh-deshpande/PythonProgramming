# 920. Number of Music Playlists
from collections import defaultdict


class Solution(object):
    def preparePlaylist(self, ans, inter, N, L, K, num_dict):

        if len(inter) == L:
            ans.append(inter)
            return

        for i in range(N):

    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        num_dict = defaultdict(int)

        for i in range(1, N + 1):
            num_dict[i] = K

        ans, inter = []
        playLists = self.preparePlaylist(ans, inter, N, L, K, num_dict)

        return len(playLists)
