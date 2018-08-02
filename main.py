import papa
import requests


def main():
    error = list()
    with open('error.txt', 'r') as f:
        firstcolumn = [line.rstrip() for line in f]  # line.split(',')[0]
    for i in firstcolumn:
        try:
            b = i
            print(b)
            df = papa.YahooFinanceHistory(b, days_back=3000).get_quote()
            df.to_csv('/home/huicheng/Documents/datas/stock_new_download/' + b + '.csv', sep='\t', encoding='utf-8', index=False)
        except (
                requests.exceptions.HTTPError, requests.exceptions.TooManyRedirects,
                requests.exceptions.ReadTimeout, requests.exceptions.ContentDecodingError) as e:
            print(str(e))
            error.append(b)
            with open('error.txt', 'w') as er:
                for each in error:
                    er.write(each)
                    er.write('\n')


if __name__ == '__main__': main()
