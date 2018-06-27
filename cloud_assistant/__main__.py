from settings import Settings, CONF_DIR

def main():
    """Main script function."""
    userSettings = Settings()
    userSettings.load_from_file(CONF_DIR)
    print(userSettings.ServerUrlDav)

if __name__ == "__main__":
    main()