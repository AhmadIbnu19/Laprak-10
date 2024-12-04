def rekursif_bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    rekursif_bubble_sort(arr, n - 1)

def main():
    data = list(map(int, input("Masukkan angka yang ingin diurutkan (pisah dengan spasi): ").split())) 
    target = int(input("Masukkan angka yang ingin dicari: "))
    print("List sebelum diurutkan:", data)
    rekursif_bubble_sort(data, len(data))
    print("List setelah diurutkan:", data)
    
    for i, index in enumerate(data):
        if index == target:
            print(f"Angka {target} ditemukan pada indeks {i}")
            break
    else:
        print(f"Angka {target} tidak ditemukan pada indeks")
    
main()