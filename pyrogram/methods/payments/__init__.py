from .get_star_gifts import GetStarGifts
from .send_star_gift import SendStarGift
from .save_star_gift import SaveStarGift
from .convert_star_gift import ConvertStarGift
from .upgrade_star_gift import UpgradeStarGift
from .get_stars_status import GetStarsStatus
from .get_stars_transactions import GetStarsTransactions
from .get_stars_balance import GetStarsBalance


class Payments(
    GetStarGifts,
    SendStarGift,
    SaveStarGift,
    ConvertStarGift,
    UpgradeStarGift,
    GetStarsStatus,
    GetStarsTransactions,
    GetStarsBalance,
):
    pass
