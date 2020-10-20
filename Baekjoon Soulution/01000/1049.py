N, M = map(int, input().split())
package = []
piece = []
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)

package = min(package)
piece = min(piece)

if 6 * piece < package:
    print(N * piece)
else:
    pack, N = divmod(N, 6)
    sum = pack * package
    if N * piece > package:
        sum += package
    else:
        sum += N * piece
    print(sum)