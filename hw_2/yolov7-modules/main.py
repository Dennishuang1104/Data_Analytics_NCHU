def run_training():
    # 定義要執行的命令以及所需的參數
    command = [
        "python", "yolov3_pytorch_modules/train.py",
        "--img", "640",
        "--batch", "16",
        "--epochs", "1",
        "--weights", "",
        "--cfg", "yolov7/models/yolov3.yaml",
        "--hyp", "yolov7/data/hyps/hyp.scratch-high.yaml",
        "--data", "yolov7_pytorch_modules/data/Transportation.yaml",
        "--cache"
    ]

    # 使用 subprocess.run 執行命令
    result = subprocess.run(command, capture_output=True, text=True)

    # 打印訓練的輸出訊息
    print("訓練過程輸出:")
    print(result.stdout)

    # 錯誤處理
    if result.returncode != 0:
        print("執行出現錯誤:")
        print(result.stderr)