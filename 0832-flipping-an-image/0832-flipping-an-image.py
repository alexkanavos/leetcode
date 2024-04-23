class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for el in image:
            el.reverse()
            for i in range(len(el)):
                el[i] = 1 - el[i]
        return image
                
        