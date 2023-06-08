import streamlit as st
import matplotlib.pyplot as plt
import time_series_method 
# Dữ liệu mẫu về người dùng đã đăng ký
registered_users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Trang đăng nhập
def login_page():
    st.title("Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    login_button = st.button("Đăng nhập")

    if login_button:
        if username == "" or password == "":
            st.error("Vui lòng nhập tên đăng nhập và mật khẩu!")
        elif username in registered_users and registered_users[username] == password:
            st.success("Đăng nhập thành công!")
            return True
        else:
            st.error("Đăng nhập thất bại!")

    return False

# Trang đăng ký
def register_page():
    st.title("Đăng ký")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    register_button = st.button("Đăng ký")

    if register_button:
        if username in registered_users:
            st.error("Tên đăng nhập đã tồn tại!")
        else:
            registered_users[username] = password
            st.success("Đăng ký thành công!")
# Xác thực đăng nhập
def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.sidebar.title("Hệ thống")
        selected_page = st.sidebar.selectbox("Chức năng", ["Đăng nhập", "Đăng ký"])

        if selected_page == "Đăng nhập":
            login_success = login_page()
            if login_success:
                st.session_state.authenticated = True
                selected_page = st.sidebar.selectbox("Chức năng", ["Trang chính", "Báo cáo thống kê"])
                if selected_page == "Báo cáo thống kê":
                    report_page()
                else:
                    main_page()
        elif selected_page == "Đăng ký":
            register_page()
    else:
        st.sidebar.title("Hệ thống")
        selected_page = st.sidebar.selectbox("Chức năng", ["Trang chính", "Báo cáo thống kê"])
        if selected_page == "Báo cáo thống kê":
            report_page()
        else:
            main_page()

# Trang chính
def main_page():
    st.title("Dự báo doanh thu")
    st.write("Dưới đây là kết quả dự báo doanh thu")
        # Nút đăng nhập

    # Nút đăng nhập
    if st.button("Đăng nhập", key="login"):
        # Di chuyển đến trang đăng nhập
        login_page()

    # Nút đăng ký
    if st.button("Đăng ký", key="register"):
        # Di chuyển đến trang đăng ký
        register_page()

    # Nút dự báo
    if st.button("Dự báo", key="forecast"):
        # Di chuyển sang trang kết quả dự báo
        report_page()


# Trang báo cáo thống kê
def report_page():
    st.title("Báo cáo biểu đồ thống kê")
    a = time_series_method.best_results.plot_diagnostics(lags=30, figsize=(16,12))
    plt.close()  # Đóng Figure trước khi sử dụng st.pyplot()
    st.pyplot(a.figure)
    
    # Hiển thị dự báo doanh thu
    st.header("Dự báo doanh thu")
    forecast_result = time_series_method.fc_all['forecast']
    st.write(forecast_result)



# Chạy ứng dụng
if __name__ == "__main__":
    authenticate()
