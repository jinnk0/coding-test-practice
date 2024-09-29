cmd = input()
w, h = cmd[0], cmd[1]

X = [2, 2, -2, -2, 1, 1, -1, -1]
Y = [1, -1, 1, -1, 2, -2, 2, -2]

W = 'abcdefgh'
H = '12345678'

idx_w = W.find(w)
idx_h = H.find(h)

place = []
for dx, dy in zip(X, Y):
    nx = idx_w + dx
    ny = idx_h + dy
    if 0<= nx < 8 and 0<= ny < 8:
        place.append(W[nx] + H[ny])

print(len(set(place)))