import pandas as pd

data_path = "data/channels.csv"

def add_channel(server_id: int, channel_id: int) -> None:

    df = pd.read_csv(data_path)
    tmp = pd.DataFrame([[server_id, channel_id, False]], columns=["server_id", "channel_id", "is_dev"])
    df = df.append(tmp)
    df.to_csv(data_path, index=False)
    return

def get_curr_channel_id(server_id: int) -> int:
    df = pd.read_csv(data_path)    
    id = df[df["server_id"] == server_id]["channel_id"]
    return int(id.iloc[0]) if len(id) == 1 else None