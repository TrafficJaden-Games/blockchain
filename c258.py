from tkinter import *
from tkinter import messagebox
from web3 import Web3
from PIL import ImageTk,Image

root=Tk()
root.title('my crypto banking app')
root.configure(background='white')

infura_url = "https://mainnet.infura.io/v3/e5b6f14fe44649c8b8309ab18d6b6051"
web3_infura_connection = Web3(Web3.HTTPProvider(infura_url))

image_logo=ImageTk.PhotoImage(Image.open("logo.jpeg"))
image_label = Label(root,image=image_logo, bg="white")
image_label.pack(side="top")

frame=Frame(root,bg="white", padx=5,pady=5)
Label(frame,text='Account Number One:', bg="white", fg="black").grid(row=0,column=0,sticky=W,pady=10)
Label(frame,text='Account Number Two:', bg="white", fg="black").grid(row=1,column=0,sticky=W,pady=10)
Label(frame,text='Private Key:', bg="white", fg="black").grid(row=2,column=0,sticky=W,pady=10)
Label(frame,text='ETH:', bg="white", fg="black").grid(row=3,column=0,sticky=W,pady=10)
Label(frame,text='Gas Price(GWEI):', bg="white", fg="black").grid(row=4,column=0,sticky=W,pady=10)
Label(frame,text='Gas Limit(GWEI):', bg="white", fg="black").grid(row=5,column=0,sticky=W,pady=10)

account1 = Entry(frame)
account2 = Entry(frame)
private_key = Entry(frame)
amount = Entry(frame)
gas_price = Entry(frame)
gas_limit = Entry(frame)

account1.grid(row=0,column=1,pady=10,padx=20)
account2.grid(row=1,column=1,pady=10,padx=20)
private_key.grid(row=2,column=1,pady=10,padx=20)
amount.grid(row=3,column=1,pady=10,padx=20)
gas_price.grid(row=4,column=1,pady=10,padx=20)
gas_limit.grid(row=5,column=1,pady=10,padx=20)

def SendETH():
	account1_id = account1.get()
	account2_id = account2.get()
	key = private_key.get()
	eth_amount = amount.get()
	gas_fee = gas_price.get()
	g_limit = gas_limit.get()
	nonce = web3_infura_connection.eth.get_transaction_count(account1_id)
	transaction = {
	"nonce":nonce,
	"to":account2_id,
	"amount":web3_infura_connection.to_wei(eth_amount,"ether"),
	"gas":int(g_limit),
	"gas_price":web3_infura_connection.to_wei(gas_fee,"gwei")
	}
	signed_transaction = web3_infura_connection.eth.account.sign_transaction(transaction,key)
	transaction_hash = web3_infura_connection.eth.send_raw_transaction(signed_transaction.raw_transaction)
	print('your transaction is successful, your transaction id is:', transaction_hash.hex())
	messagebox.showInfo("transaction status", "transaction successful, verify your metamask wallet.")

frame.pack()

transfer_eth = Button(root, text="transfer ETH", command=SendETH, highlightbackground="white", width="15")
transfer_eth.pack()

root.mainloop()