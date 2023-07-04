if __name__ == "__main__":
    forex_name = input("what is the name of stock or index or pair ?")
    directionStr = input("1 for buy , 2 for sell [1]?")
    direction = 1
    if directionStr is not None and directionStr != "" :
        
        direction = int(directionStr)
    
    entry_point = float(input("what is the entry point price ?"))
    lot_size = 100000
    lot_sizeStr = input("what is the lot size [100000]?")
    if lot_sizeStr is not None and lot_sizeStr != "":
        lot_size = int(lot_sizeStr)
    volume = 0.01
    volumeStr = input("what is the volume you will {} {}".format(  ("buy" if direction == 1 else "sell") , "[0.01]?"))
    if volumeStr is not None and volumeStr != "":
        volume = float(volumeStr)
    price_to_usd = 1.0
    price_to_usdStr = input("what is the currency used price to USD (1 means your entry point is in USD) [1.0]? ")
    if price_to_usdStr is not None and price_to_usdStr != "":
        price_to_usd = float(price_to_usdStr)
    amount_to_win = 5.0
    amount_to_winStr = input("what is the amount to win (take profit) in USD [5.0]?")
    if amount_to_winStr is not None and amount_to_winStr != "":
        amount_to_win  = float(amount_to_winStr)
    
    amount_to_loss = 20.0
    amount_to_lossStr = input("what is the amount ot loss (stop loss) in USD [20.0]?")
    if amount_to_lossStr is not None and amount_to_lossStr != "":
        amount_to_loss = float(amount_to_lossStr)
    print ("name : ", forex_name)
    print ("direction : ",("buy" if direction == 1 else "sell"))
    print("entry point : ",entry_point)
    print("lot size : ", lot_size)
    print("volume : ", volume)
    print("target currency usd price : ",price_to_usd)
    print("amount to win : ",amount_to_win)
    print("amount to loss : ",amount_to_loss)

    