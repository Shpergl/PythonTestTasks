import scrapy
from prettytable import PrettyTable


class WorldCup2018Spider(scrapy.Spider):
    name = "WorldCup2018"
    result = {}

    def start_requests(self):
        urls = [
            ('WilliamHill', ('http://sports.williamhill.com/bet/en-gb/betting/e/1644903/'
                             'World+Cup+2018+-+Outright.html')),
            ('Paddypower', ('http://www.paddypower.com/football/international-football/'
                            'world-cup-2018?ev_oc_grp_ids=1828129'))
        ]
        for site, url in urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse_teams,
                                 meta={
                                  'site': site,
                                 })

    def parse_teams(self, response):

        # Selectors for WilliamHill web site.
        table_list_William = response.css("#ip_marketBody10146188 tr td")
        if table_list_William:

            for item in table_list_William:
                team_name = item.css(".eventselection::text").extract_first().strip()
                probability = item.css(".eventprice::text").extract_first().strip()

                if probability and team_name:
                    site = {
                        response.meta.get('site'): probability
                    }
                    self.result = self.add_site(self.result, team_name, site)

        # Selectors for PaddyPower web site.
        table_list_Paddypower = response.css("div.fb-sub-content span.odd")
        if table_list_Paddypower:
            for item in table_list_Paddypower:
                team_name = item.css("a span.odds-label::text").extract_first()
                probability = item.css("a span.odds-value::text").extract_first()

                if probability and team_name:
                    site = {
                        response.meta.get('site'):probability.strip()
                    }
                    self.result = self.add_site(self.result, team_name.strip(), site)

        self.display_result(self.result)

    def display_result(self, result_dict):

        if result_dict:
            t = PrettyTable(['Country', 'WilliamHill', 'Paddypower'])

            for team, prop_dict in sorted(result_dict.items()):
                t.add_row([team, prop_dict.get('WilliamHill'), prop_dict.get('Paddypower')])
            print (t)

    def add_site(self, resulted_dict, team_name, site):

        if team_name and site:
            site_dict = resulted_dict.get(team_name)
            if not site_dict:
                resulted_dict[team_name] = site
            else:
                d = site_dict.copy()
                d.update(site)
                resulted_dict[team_name] = d

            return resulted_dict


