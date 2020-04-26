def book_tickets(n, bookings):
    arr = [0]*(n+1)
    for i in range(len(bookings)):
        start, end, k = bookings[i]
        arr[start-1] += k
        arr[end] -= k
    for i in range(1, n+1):
        arr[i] = arr[i]+arr[i-1]
    return arr[:n]

B = [[1,2,10], [2,3,15], [4,5,20]]
print(book_tickets(5, B));