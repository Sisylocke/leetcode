class Solution:

    @staticmethod
    def findMedianSortedArrays(A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, mid = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = mid - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    lmax = B[j-1]
                elif j == 0:
                    lmax = A[i-1]
                else:
                    lmax = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return lmax

                if i == m:
                    rmin = B[j]
                elif j == n:
                    rmin = A[i]
                else:
                    rmin = min(A[i], B[j])

                return (lmax + rmin) / 2.0
