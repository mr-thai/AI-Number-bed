import matplotlib.pyplot as plt

print("hello world")


def plot_actual_vs_predicted_by_dept(test_data, date_col, actual_col, pred_col, dept_configs):

    num_plots = len(dept_configs)
    
    fig, axes = plt.subplots(nrows=num_plots, ncols=1, figsize=(12, 4 * num_plots), sharex=True)

    if num_plots == 1:
        axes = [axes]

    for i, config in enumerate(dept_configs):
        dept_data = test_data[test_data[config['filter_col']] == 1].sort_values(date_col)

        # Vẽ đường Thực tế
        axes[i].plot(dept_data[date_col], dept_data[actual_col], 
                     label="Thực tế", marker=".", color="#1f77b4")
        # Vẽ đường Dự báo
        axes[i].plot(dept_data[date_col], dept_data[pred_col], 
                     label="Dự báo", marker=".", color=config.get('pred_color', '#ff7f0e'))

        # Thiết lập thông số hiển thị
        axes[i].set_title(f"{config['title']}: Tập Test")
        axes[i].set_ylabel("Số giường")
        axes[i].legend()
        axes[i].grid(axis="y", linestyle="--", alpha=0.5)

    # Thiết lập nhãn trục X cho biểu đồ cuối cùng
    axes[-1].set_xlabel("Time")

    plt.tight_layout()
    plt.show()