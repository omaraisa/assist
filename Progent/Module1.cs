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
using ArcGIS.Desktop.Core;
using ArcGIS.Desktop.Framework.Events;

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
            UpdateTheme(FrameworkApplication.ApplicationTheme);
            ThemeChangedEvent.Subscribe(OnThemeChanged);
            return base.Initialize();
        }

        private void OnThemeChanged(ThemeChangedEventArgs args)
        {
            UpdateTheme(args.NewTheme);
        }

        private void UpdateTheme(ApplicationTheme theme)
        {
            // Update the ProgentLogo resource
            var lightImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo.png"));
            var darkImage = new BitmapImage(new Uri("pack://application:,,,/Progent;component/Images/logo-bright.png"));
            var currentImage = theme == ApplicationTheme.Dark ? darkImage : lightImage;

            if (FrameworkApplication.Current.Resources.Contains("ProgentLogo"))
            {
                FrameworkApplication.Current.Resources.Remove("ProgentLogo");
            }
            FrameworkApplication.Current.Resources.Add("ProgentLogo", currentImage);

            // Update the ribbon button's icon
            var button = FrameworkApplication.GetPlugInWrapper("Progent_Dockpane_ShowButton") as IPlugInWrapper;
            if (button != null)
            {
                button.LargeImage = currentImage;
                button.SmallImage = currentImage;
            }
        }

        #endregion Overrides

    }
}
