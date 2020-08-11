from ssdpatent.models import SSDPatent


def save_file(n):
    all_patent = SSDPatent.objects.all()
    i = 0
    for patent in all_patent:
        i += 0
        print(patent.imgtitle)
        if i >= n:
            break


if __name__ == '__main__':
    save_file(10)
