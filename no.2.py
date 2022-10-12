import scrapy

class TechnoSpider(scrapy.Spider):
    name ='techno'
    allowed_domains = ['sindonews.com']
    start_urls = ['https://nasional.sindonews.com/']

    def parse(self, response):
        cont = response.css('.homelist-new')

        #collecting data
        kat = cont.css('.homelist-channel')
        tgl = cont.css('.homelist-date')
        judul = cont.css('.homelist-title')
        desk = cont.css('.homelist-desc')
        c=0
        
        #combining the results
        for review in kat:
            yield{'Kategori':''.join(review.xpath('.//text()').extract()),
                  'tgl':''.join(tgl.xpath('.//text()').extract()),
                  'Judul':''.join(judul.xpath('.//text()').extract()),
                  'link':''.join(judul.xpath('.//text()').extract()),
                  'deskripsi':''.join(desk.xpath('.//text()').extract()),
                  }
            c=c+1
