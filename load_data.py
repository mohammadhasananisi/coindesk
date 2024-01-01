
from bs4 import BeautifulSoup
import time
import requests
from db.con import DB
from mobile_data import clone_mobile_data
import datetime

class LoadData(DB):

    def __init__(self) -> None:
        super(LoadData, self).__init__()
        DB.__init__(self)
        self.url = "https://production.api.coindesk.com/v2/tb/price/ticker?assets=BTC,ETH,XRP,BCH,EOS,XLM,LTC,ADA,XMR,DASH,IOTA,TRX,NEO,ETC,XEM,ZEC,BTG,LSK,QTUM,BSV,DOGE,DCR,USDT,USDC,LINK,XTZ,ZRX,DAI,BAT,OXT,ALGO,ATOM,KNC,OMG,ANT,REP,BAND,BTT,MANA,FET,ICX,KAVA,LRC,MKR,MLN,NANO,NMR,PAXG,USDP,SC,STORJ,WAVES,FIL,CVC,DNT,REN,BNT,WBTC,GRT,UNI,DOT,YFI,AAVE,MATIC,AMP,CELO,COMP,CRV,RLC,KSM,NKN,SHIB,SKL,SNX,LUNC,UMA,ICP,SOL,AVAX,UST,ENJ,IOTX,AXS,XYO,SUSHI,ANKR,CHZ,LPT,COTI,KEEP,SAND,GALA,APE,CRO,ACHP,JASMY,REQ,SLP,NEAR,MBOX,POLIS,MOVR,POLS,QUICK,MINA,IMX,XEC,NEXO,RUNE,QNT,VET,CAKE,BNB,THETA,HBAR,FTM,RVN,ZIL,DGB,FTT,ENS,WRX,WAXP,EGLD,BUSD,CEL,OP,LUNA,RAY,FLOW,AUDIO,CKB,VGX,YGG,CHR,STMX,SXP,INJ,JOE,POLY,STX,SFP,FARM,XVG,CLV,WOO,GLMR,STEEM,RARE,IDEX,SRM,PYR,MIR,SYS,ALPACA,QSP,SCRT,SUN,APT,MASK,DYDX,CVX,GMT,CTSI,METIS,FORTH,RBN,SAMO,SPELL,LDO,ARB,BLUR,GAS,RACA,BABYDOGE,FLOKI,HOT,BFC,KISHU,ELON,SAITAMA,REEF,CEEK,ATLAS,LOOKS,WIN,ONE,DENT,GST,TWT,HNT,AGLD,BTRST,ETHW,ILV,RARI,STG,SYN,TOKE,BLZ,FLR,FIS,GNS,ID,PEPE,DIA,TLM,XCN,BIT,RPL,RNDR,1INCH,BAL,T,GNO,ASTR,GLM,OCEAN,BICO,CELR,LQTY,TRAC,ZEN,API3,PLA,AXL,HFT,MC,C98,GAL,GTC,RAD,POWR,POND,ALICE,TRU,OGN,DAR,BADGER,GHST,LCX,ARPA,MXC,PERP,LOKA,BOBA,BOND,ALCX,KP3R,TON,AR,AVA,BONE,BONK,CORE,CSPR,DG,ERN,FXS,GMX,GT,GUSD,HMT,HT,KCS,KLAY,LEO,MPL,OKB,PIT,OSMO,RLY,SANTOS,SUI,SWEAT,TUSD,TVK,UNFI,USDD,VLX,WEMIX,XDC,XRD,FB,BRISE,KAS,XEN,HAM,TAMA,KDA,CFX,VRA,BDX,RDNT,WLD,AGIX,PYUSD,MOON,SEI,AKT,MAGIC,SNT,ALPHA,ALI,CQT,HIGH,AERGO,GODS,ZBC,ACA,MDT,LIT,QI,AURORA,TOMI,XCH"

    def get_data(self):
        try:
            response = requests.get(self.url)

            data = response.json()
            data = data['data']
            for d in data:

                ohlc = data[d]['ohlc']
                change = data[d]['change']['percent']
                self.set_data_db(
                    name=data[d]['name'],
                    open=ohlc['o'],
                    high=ohlc['h'],
                    low=ohlc['l'],
                    close=ohlc['c'],
                    change_percent=change,
                    created_at=self.get_current_time(),
                )

        except Exception as e:
            print(e)
        finally:
            return self.get_data_db()

    def get_current_time(self):
        return datetime.datetime.now()


    # def set_mobile_data(self):
    #     try:
    #         data = clone_mobile_data()
    #         for d in data:
    #             self.set_mobile_data_db(
    #                 id=d['id'],
    #                 title=d['title_fa'],
    #                 black=d['black'],
    #                 white=d['white'],
    #                 pink=d['pink'],
    #                 gold=d['gold'],
    #                 silver=d['silver'],
    #             )
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         return True

