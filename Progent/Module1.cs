using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using ArcGIS.Core.CIM;
using ArcGIS.Core.Data;
using ArcGIS.Core.Geometry;
using ArcGIS.Desktop.Catalog;
using ArcGIS.Desktop.Core;
using ArcGIS.Desktop.Editing;
using ArcGIS.Desktop.Extensions;
using ArcGIS.Desktop.Framework;
using ArcGIS.Desktop.Framework.Contracts;
using ArcGIS.Desktop.Framework.Dialogs;
using ArcGIS.Desktop.Framework.Threading.Tasks;
using ArcGIS.Desktop.Layouts;
using ArcGIS.Desktop.Mapping;
using System.Windows.Media;
using System.Windows.Media.Imaging;

namespace Progent
{
    internal class Module1 : Module
    {
        private static Module1 _this = null;

        /// <summary>
        /// Retrieve the singleton instance to this module here
        /// </summary>
        public static Module1 Current => _this ??= (Module1)FrameworkApplication.FindModule("Progent_Module");

        #region Overrides
        /// <summary>
        /// Called by Framework when ArcGIS Pro is closing
        /// </summary>
        /// <returns>False to prevent Pro from closing, otherwise True</returns>
        protected override bool CanUnload()
        {
            //TODO - add your business logic
            //return false to ~cancel~ Application close
            return true;
        }

        /// <summary>
        /// Called by Framework when the module is initialized.
        /// </summary>
        /// <returns>true if the module can be initialized, false otherwise</returns>
        protected override bool Initialize()
        {
            FrameworkApplication.ActiveThemeChanged += OnActiveThemeChanged;
            UpdateImageSources();
            return base.Initialize();
        }


        private void OnActiveThemeChanged(ApplicationTheme theme)
        {
            UpdateImageSources(theme);

            //Update the button's icon
            var button = FrameworkApplication.Ribbon.FindControl("Progent_Dockpane_ShowButton") as IPlugInWrapper;
            if (button != null)
            {
                if (theme == ApplicationTheme.Dark)
                {
                    button.LargeImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo-bright.png"));
                    button.SmallImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo-bright.png"));
                }
                else
                {
                    button.LargeImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo.png"));
                    button.SmallImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo.png"));
                }
            }
        }

        /// <summary>
        /// Updates the image sources in the resource dictionary based on the current theme.
        /// </summary>
        /// <param name="theme"></param>
        private void UpdateImageSources(ApplicationTheme? theme = null)
        {
            if (theme == null)
                theme = FrameworkApplication.ApplicationTheme;

            // Define the image sources for light and dark themes
            var lightImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo.png"));
            var darkImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo-bright.png"));

            // Get the current image source based on the theme
            var currentImage = theme == ApplicationTheme.Dark ? darkImage : lightImage;

            // Remove the existing resource if it exists
            if (FrameworkApplication.Application.Resources.Contains("ProgentLogo"))
            {
                FrameworkApplication.Application.Resources.Remove("ProgentLogo");
            }

            // Add the new image source to the resource dictionary
            FrameworkApplication.Application.Resources.Add("ProgentLogo", currentImage);
        }

        #endregion Overrides

    }
}
