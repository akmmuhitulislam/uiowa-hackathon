
import pandas as pd
import matplotlib.pyplot as plt
n = -1
i=0
look = "action"
ff = "truth"
for i in range(1000,1063):
        dd_df = pd.read_csv(f"results/logs/log_episode_{i}.csv")
        dd_df = dd_df.fillna(0)
        # dd_df = dd_df.drop("date", axis=1)
        dd_df = dd_df.astype('float')

        fig,ax = plt.subplots()
        ax.plot(dd_df.index.unique()[i:n],
                dd_df[look][i:n],
                color="red")

        ax.set_xlabel("Steps/Days", fontsize = 14)
        # set y-axis label
        ax.set_ylabel(look,
                color="red",
                fontsize=14)

        ax2=ax.twinx()

        ax2.plot(dd_df.index.unique()[i:n],
                dd_df[ff][i:n],color="blue",alpha = 0.5)
        ax2.set_ylabel(f"{ff}",color="blue",fontsize=14)


        fig.savefig(f'plots/{i}_actionXtruth.jpg',
                format='jpeg',
                dpi=100,
                bbox_inches='tight')


# dd_df.reward.plot()
# dd_df.close.plot()
#dd_df.transactions.plot()
#dd_df.total_asset[200]
#tt = dd_df.transactions
#dd_df.action.plot()
#dd_df.cash.plot()
# dd_df.owned_shorts.plot()
#dd_df.action.count(0)